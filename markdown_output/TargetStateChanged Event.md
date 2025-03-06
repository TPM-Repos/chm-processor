       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TargetStateChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Transition Class](topic11757.md) : TargetStateChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the [TargetState](topic11769.md) property is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TargetStateChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Transition](topic11757.md)
    Dim handler As EventHandler
     
    AddHandler instance.TargetStateChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler TargetStateChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Transition Class](topic11757.md)   
[Transition Members](topic11758.md)


