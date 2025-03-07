Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetEnumerator Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectComponentSets Class](topic4143.md) : GetEnumerator Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets an enumerator which can enumerate over the collection. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetEnumerator() As IEnumerator(Of ProjectComponentSet)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectComponentSets](topic4143.md)
    Dim value As IEnumerator(Of ProjectComponentSet)
     
    value = instance.GetEnumerator()  
  
C#|   
---|---  
      
    
    public IEnumerator<ProjectComponentSet> GetEnumerator()  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectComponentSets Class](topic4143.md)   
[ProjectComponentSets Members](topic4144.md)


