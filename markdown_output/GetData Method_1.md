Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ImportedDataTable Class](topic3483.md) : GetData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns the cached data from the design master. This is much faster than re-loading from file. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetData() As Object(,)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ImportedDataTable](topic3483.md)
    Dim value() As Object
     
    value = instance.GetData()  
  
C#|   
---|---  
      
    
    public object[,] GetData()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ImportedDataTable Class](topic3483.md)   
[ImportedDataTable Members](topic3484.md)


