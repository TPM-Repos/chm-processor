Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyBeginRelease Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyBeginRelease Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentTrackingId_
    The tracking identifier of the component.

Glossary Item Box

Called when the release of an evaluated component has started. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyBeginRelease( _
       ByVal _componentTrackingId_ As Guid _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim componentTrackingId As Guid
     
    instance.NotifyBeginRelease(componentTrackingId)  
  
C#|   
---|---  
      
    
    void NotifyBeginRelease( 
       Guid _componentTrackingId_
    )  
  
#### Parameters

 _componentTrackingId_
    The tracking identifier of the component.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


