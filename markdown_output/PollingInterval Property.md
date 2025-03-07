Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PollingInterval Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupPollingConnectorBase<T> Class](topic1878.md) : PollingInterval Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the polling interval. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Property PollingInterval As TimeSpan  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupPollingConnectorBase(Of T)](topic1878.md)
    Dim value As TimeSpan
     
    instance.PollingInterval = value
     
    value = instance.PollingInterval  
  
C#|   
---|---  
      
    
    protected TimeSpan PollingInterval {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupPollingConnectorBase<T> Class](topic1878.md)   
[GroupPollingConnectorBase<T> Members](topic1879.md)


