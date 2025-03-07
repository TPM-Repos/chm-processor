Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaiseStarted Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ConnectorBase Class](topic1834.md) : RaiseStarted Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data.

Glossary Item Box

Raises the [Started](topic1847.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaiseStarted( _
       ByVal _e_ As EventArgs _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ConnectorBase](topic1834.md)
    Dim e As EventArgs
     
    instance.RaiseStarted(e)  
  
C#|   
---|---  
      
    
    protected void RaiseStarted( 
       EventArgs _e_
    )  
  
#### Parameters

 _e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ConnectorBase Class](topic1834.md)   
[ConnectorBase Members](topic1835.md)


