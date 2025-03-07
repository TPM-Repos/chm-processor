Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCachedTableData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectDataTable Class](topic4282.md) : GetCachedTableData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the cached table data from the design master. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetCachedTableData() As Object(,)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDataTable](topic4282.md)
    Dim value() As Object
     
    value = instance.GetCachedTableData()  
  
C#|   
---|---  
      
    
    public object[,] GetCachedTableData()  
  
#### Return Value

A zero-based two dimensional array of values.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDataTable Class](topic4282.md)   
[ProjectDataTable Members](topic4283.md)


