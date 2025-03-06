Specifying Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationRequest Interface](topic1778.md) : Specifying Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when the [ISpecificationRequest](topic1778.md) is being processed by DriveWorks. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Specifying As EventHandler(Of SpecificationContextEventArgs)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationRequest](topic1778.md)
    Dim handler As EventHandler(Of SpecificationContextEventArgs)
     
    AddHandler instance.Specifying, handler  
  
C#|   
---|---  
      
    
    event EventHandler<SpecificationContextEventArgs> Specifying  
  
# Event Data

The event handler receives an argument of type [SpecificationContextEventArgs](topic11284.md) containing data related to this event. The following **SpecificationContextEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Context](topic11291.md)| Get the specification context.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationRequest Interface](topic1778.md)   
[ISpecificationRequest Members](topic1779.md)


