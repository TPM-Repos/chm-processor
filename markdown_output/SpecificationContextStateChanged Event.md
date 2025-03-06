SpecificationContextStateChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ChildSpecificationList Class](topic7547.md) : SpecificationContextStateChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a child specification's state is changed. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event SpecificationContextStateChanged As EventHandler(Of SpecificationContextEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ChildSpecificationList](topic7547.md)
    Dim handler As EventHandler(Of SpecificationContextEventArgs)
     
    AddHandler instance.SpecificationContextStateChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler<SpecificationContextEventArgs> SpecificationContextStateChanged  
  
# Event Data

The event handler receives an argument of type [SpecificationContextEventArgs](topic11284.md) containing data related to this event. The following **SpecificationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic11291.md)| Get the specification context.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ChildSpecificationList Class](topic7547.md)   
[ChildSpecificationList Members](topic7548.md)


