Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetPlaceholderData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RollupDataTable Class](topic5240.md) : GetPlaceholderData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the placeholder data for the table. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetPlaceholderData() As String(,)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RollupDataTable](topic5240.md)
    Dim value() As String
     
    value = instance.GetPlaceholderData()  
  
C#|   
---|---  
      
    
    public string[,] GetPlaceholderData()  
  
#### Return Value

The placeholder data without the table column headings. [ProjectDataTable.GetCachedTableData](topic4292.md) should be used to retrieve the complete table.

# Remarks

This data can be used for getting meaningful results when building rules.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RollupDataTable Class](topic5240.md)   
[RollupDataTable Members](topic5241.md)


