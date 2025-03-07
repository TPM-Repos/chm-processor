Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Dependencies Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) : Dependencies Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets the identifiers of all of the driven components on which the specification is dependent. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Dependencies As Guid()  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleaseComponentsResults](topic6300.md)
    Dim value() As Guid
     
    value = instance.Dependencies  
  
C#|   
---|---  
      
    
    public Guid[] Dependencies {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)


