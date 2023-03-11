#!/usr/bin/env python3

source_file = "cubeblocklist.txt"
target_file = "target.cs"

def main():
    with open(source_file, "r") as source:
        with open(target_file, "w") as target:
            for line in source:
                _l = line.split("/")
                render: str = builder(_l)
                target.write(render)
                print(render)

def builder(line: list) -> str:
    subtypeid = line[1]
    try:
        count = line[2]
    except IndexError:
        count = 10
    return f"""
    new BlockDef()
    {{
        BlockName = "CubeBlock/{subtypeid}",
            BlockActions = new[]
            {{
                new BlockAction
                {{
                    Action = ReplaceComponent,
                    Component = "MyObjectBuilder_Component/TitaniumNanocomposite",
                    Index = 1,
                    Count = {count}
                }},
                new BlockAction
                {{
                    Action = ChangeComponentDeconstructId,
                    Component = "MyObjectBuilder_Ore/Scrap",
                    Index = 1
                }},
                new BlockAction
                {{
                    Action = ChangeCriticalComponentIndex,
                    Index = 1
                }},
            }}
    }},
    """

if __name__ == "__main__":
    main()
