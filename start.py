#!/usr/bin/env python3

source_file = "cubeblocklist.txt"
target_file = "target.cs"

def main():
    with open(source_file, "r") as source:
        with open(target_file, "w") as target:
            for line in source:
                _l = line.split("/")
                subtypeid = _l[1]
                try:
                    count = _l[2]
                except IndexError:
                    count = 10
                render = f"""
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
                target.write(render)
                print(render)

if __name__ == "__main__":
    main()
