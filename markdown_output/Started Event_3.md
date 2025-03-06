Started Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [IConnector Interface](topic1697.md) : Started Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a connector has started. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Started As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IConnector](topic1697.md)
    Dim handler As EventHandler
     
    AddHandler instance.Started, handler  
  
C#|   
---|---  
      
    
    event EventHandler Started  
  
# Remarks

Implementors should raise this event when the connector is started by the [Start](topic1702.md) method. A connector should never start itself.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IConnector Interface](topic1697.md)   
[IConnector Members](topic1698.md)


