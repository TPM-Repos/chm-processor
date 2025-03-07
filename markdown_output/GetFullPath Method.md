Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetFullPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectConstantCategory Class](topic4219.md) : GetFullPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the fully qualified path to the project category. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetFullPath() As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectConstantCategory](topic4219.md)
    Dim value As String
     
    value = instance.GetFullPath()  
  
C#|   
---|---  
      
    
    public string GetFullPath()  
  
#### Return Value

A string of the form "RootCategoryName\ChildCategory0\ChildCategory1\ChildCategory...\ThisCategory".

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectConstantCategory Class](topic4219.md)   
[ProjectConstantCategory Members](topic4220.md)


