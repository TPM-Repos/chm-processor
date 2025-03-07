Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OpenRequested Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : OpenRequested Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the opening of an existing specification is requested. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event OpenRequested As EventHandler(Of SpecificationDetailsEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler(Of SpecificationDetailsEventArgs)
     
    AddHandler instance.OpenRequested, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SpecificationDetailsEventArgs> OpenRequested  
  
# Event Data

The event handler receives an argument of type [SpecificationDetailsEventArgs](topic11322.md) containing data related to this event. The following **SpecificationDetailsEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[SpecificationDetails](topic11332.md)| Gets the specification details instance which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


