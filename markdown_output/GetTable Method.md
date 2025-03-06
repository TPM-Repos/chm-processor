![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTable Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic4322.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTables Class](topic4311.md) : GetTable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the table to get.

Glossary Item Box

Gets the table with the specified name. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTable( _
       ByVal _name_ As String _
    ) As [ProjectDataTable](topic4282.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTables](topic4311.md)
    Dim name As String
    Dim value As [ProjectDataTable](topic4282.md)
     
    value = instance.GetTable(name)  
  
C#|   
---|---  
      
    
    public [ProjectDataTable](topic4282.md) GetTable( 
       string _name_
    )  
  
#### Parameters

 _name_
    The name of the table to get.

#### Return Value

The data table with the specified name.

# ![](dotnetimages/collapse.gif)Exceptions

Exception| Description  
---|---  
[ItemNotFoundException](topic3571.md)| Thrown if a data table with the specified name does not exist.  
System.ArgumentNullException| Thrown if the name argument is a null reference.  
  
# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectDataTables Class](topic4311.md)   
[ProjectDataTables Members](topic4312.md)

©2024 DriveWorks Ltd. All Rights Reserved.
