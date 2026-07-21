from pathlib import Path
import re
import json


def split_markdown_by_heading(md_path, max_chunk_size=800):
    """
    根据 Markdown 标题进行分块。

    参数：
        md_path: markdown 文件路径
        max_chunk_size: 每个chunk最大字符数

    返回：
        List[dict]
    """

    text = Path(md_path).read_text(encoding="utf-8")

    # 按一级、二级、三级标题切分
    pattern = r'(?=^#{1,3}\s+)'

    sections = re.split(pattern, text, flags=re.MULTILINE)

    chunks = []

    chunk_id = 0

    for section in sections:

        section = section.strip()

        if not section:
            continue

        lines = section.splitlines()

        title = lines[0]

        body = "\n".join(lines[1:]).strip()

        if not body:
            continue

        # 长章节继续切
        if len(body) <= max_chunk_size:

            chunks.append({
                "chunk_id": chunk_id,
                "title": title,
                "text": body
            })

            chunk_id += 1

        else:

            for i in range(0, len(body), max_chunk_size):

                chunks.append({
                    "chunk_id": chunk_id,
                    "title": title,
                    "text": body[i:i + max_chunk_size]
                })

                chunk_id += 1

    return chunks


def save_chunks(chunks, output_path):

    Path(output_path).write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )


if __name__ == "__main__":

    # hazard-agent 根目录
    project_root = Path(__file__).resolve().parent.parent

    # Markdown 文件
    md_path = project_root / "knowledge" / "reports" / "中信鑫泰能源有限公司-91140825073076073E-隐患排查报告_2079119303565602816.md"

    # 输出 chunks.json
    output_path = project_root / "knowledge" / "reports" / "chunks.json"

    chunks = split_markdown_by_heading(md_path)

    save_chunks(chunks, output_path)

    print(f"共生成 {len(chunks)} 个 Chunk")