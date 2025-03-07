Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ProjectClosing Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : ProjectClosing Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised just before the current project is about to be closed, but before saving (which may or may not happen). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ProjectClosing As EventHandler(Of ProjectClosingEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler(Of ProjectClosingEventArgs)
     
    AddHandler instance.ProjectClosing, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ProjectClosingEventArgs> ProjectClosing  
  
# Event Data

The event handler receives an argument of type [ProjectClosingEventArgs](topic4086.md) containing data related to this event. The following **ProjectClosingEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[IsSaving](topic4093.md)| Gets whether the project is to be saved or not.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


