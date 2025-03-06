![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateDataTable(Type,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4319.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTables Class](topic4311.md) > [CreateDataTable Method](topic4317.md) : CreateDataTable(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tableType_
    The type of the table to add.

_name_
    The name of the table to add.

Glossary Item Box

Creates and adds a new table to the project. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateDataTable( _
       ByVal _tableType_ As Type, _
       ByVal _name_ As String _
    ) As [ProjectDataTable](topic4282.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTables](topic4311.md)
    Dim tableType As Type
    Dim name As String
    Dim value As [ProjectDataTable](topic4282.md)
     
    value = instance.CreateDataTable(tableType, name)  
  
C#|   
---|---  
      
    
    public [ProjectDataTable](topic4282.md) CreateDataTable( 
       Type _tableType_ ,
       string _name_
    )  
  
#### Parameters

 _tableType_
    The type of the table to add.
_name_
    The name of the table to add.

#### Return Value

The newly created table.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[ItemExistsException](topic3561.md)| A table with the given name already exists.  
System.ArgumentOutOfRangeException| The type specified in tableType does not inherit from [ProjectDataTable](topic4282.md) or isn't defined in a extension library.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDataTables Class](topic4311.md)   
[ProjectDataTables Members](topic4312.md)   
[Overload List](topic4317.md)

©2024 DriveWorks Ltd. All Rights Reserved.
