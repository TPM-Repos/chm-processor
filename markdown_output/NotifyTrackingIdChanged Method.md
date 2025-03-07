Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyTrackingIdChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyTrackingIdChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newTrackingId_
    The replacement tracking identifier.

Glossary Item Box

Called when the current component is going to be used to overwriting an existing component and so the tracking id needs to be changed 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyTrackingIdChanged( _
       ByVal _newTrackingId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim newTrackingId As Guid
     
    instance.NotifyTrackingIdChanged(newTrackingId)  
  
C#|   
---|---  
      
    
    void NotifyTrackingIdChanged( 
       Guid _newTrackingId_
    )  
  
#### Parameters

 _newTrackingId_
    The replacement tracking identifier.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


