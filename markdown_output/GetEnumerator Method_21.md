Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ProjectAnnotationCollection Class](topic14419.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator which can enumerate over the items in the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of ProjectAnnotation)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectAnnotationCollection](topic14419.md)
    Dim value As IEnumerator(Of ProjectAnnotation)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<ProjectAnnotation> GetEnumerator()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectAnnotationCollection Class](topic14419.md)   
[ProjectAnnotationCollection Members](topic14420.md)


