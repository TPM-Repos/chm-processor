Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnStop Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [GroupPollingConnectorBase<T> Class](topic1878.md) : OnStop Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Stops the polling thread. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub OnStop()   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupPollingConnectorBase(Of T)](topic1878.md)
     
    instance.OnStop()  
  
C#|   
---|---  
      
    
    protected override void OnStop()  
  
# Remarks

Generally this method shouldn't be overridden. If it is overridden then it should be called by the overriding method.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupPollingConnectorBase<T> Class](topic1878.md)   
[GroupPollingConnectorBase<T> Members](topic1879.md)


