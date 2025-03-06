       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Stopped Event   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic1848.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ConnectorBase Class](topic1834.md) : Stopped Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Occurs when a connector has stopped. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event Stopped As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectorBase](topic1834.md)
    Dim handler As EventHandler
     
    AddHandler instance.Stopped, handler  
  
C#|   
---|---  
      
    
    public event EventHandler Stopped  
  
# Remarks

Implementors should raise this event when the connector is stopped by the [Stop](topic1703.md) method, or when the connector is stopped internally for any reason.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectorBase Class](topic1834.md)   
[ConnectorBase Members](topic1835.md)

©2024 DriveWorks Ltd. All Rights Reserved.
