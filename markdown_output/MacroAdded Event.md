Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
MacroAdded Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationMacros Class](topic11467.md) : MacroAdded Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a new macro is added. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event MacroAdded As EventHandler(Of SpecificationMacroEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationMacros](topic11467.md)
    Dim handler As EventHandler(Of SpecificationMacroEventArgs)
     
    AddHandler instance.MacroAdded, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SpecificationMacroEventArgs> MacroAdded  
  
# Event Data

The event handler receives an argument of type [SpecificationMacroEventArgs](topic11456.md) containing data related to this event. The following **SpecificationMacroEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Macro](topic11466.md)| Gets the macro which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationMacros Class](topic11467.md)   
[SpecificationMacros Members](topic11468.md)


