![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_TTableType_
    The type of table to create.

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
AddTable<TTableType>(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3143.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupDataTables Class](topic3136.md) > [AddTable Method](topic3142.md) : AddTable<TTableType>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name to give the new table.

Glossary Item Box

Adds a table of the specified type to the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function AddTable(Of TTableType As [GroupDataTable](topic3110.md))( _
       ByVal _name_ As String _
    ) As TTableType  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupDataTables](topic3136.md)
    Dim name As String
    Dim value As TTableType
     
    value = instance.AddTable(Of TTableType)(name)  
  
C#|   
---|---  
      
    
    public TTableType AddTable<TTableType>( 
       string _name_
    )
    where TTableType: [GroupDataTable](topic3110.md)  
  
#### Parameters

 _name_
    The name to give the new table.

#### Type Parameters

_TTableType_
    The type of table to create.

#### Return Value

The created table.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupDataTables Class](topic3136.md)   
[GroupDataTables Members](topic3137.md)   
[Overload List](topic3142.md)

©2024 DriveWorks Ltd. All Rights Reserved.
