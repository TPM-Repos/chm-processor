Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectDimensionCollection Class](topic14506.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an object which can enumerate over the items in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of ProjectDimension)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectDimensionCollection](topic14506.md)
    Dim value As IEnumerator(Of ProjectDimension)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<ProjectDimension> GetEnumerator()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectDimensionCollection Class](topic14506.md)   
[ProjectDimensionCollection Members](topic14507.md)


