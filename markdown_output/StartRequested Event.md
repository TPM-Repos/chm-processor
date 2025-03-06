       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
StartRequested Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) : StartRequested Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the start of a new specification is requested. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event StartRequested As EventHandler(Of ProjectDetailsEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim handler As EventHandler(Of ProjectDetailsEventArgs)
     
    AddHandler instance.StartRequested, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<ProjectDetailsEventArgs> StartRequested  
  
# Event Data

The event handler receives an argument of type [ProjectDetailsEventArgs](topic11112.md) containing data related to this event. The following **ProjectDetailsEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[ProjectDetails](topic11122.md)| Gets the project details instance which is the target of the event.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)


