Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DrawingsToDefer Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentController Class](topic6252.md) : DrawingsToDefer Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the name of the drawings that should be flagged for generation at a later stage. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property DrawingsToDefer As IEnumerable(Of String)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentController](topic6252.md)
    Dim value As IEnumerable(Of String)
     
    value = instance.DrawingsToDefer  
  
C#|   
---|---  
      
    
    public IEnumerable<string> DrawingsToDefer {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentController Class](topic6252.md)   
[ReleaseComponentController Members](topic6253.md)


