Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyComponentSetLoadFailed Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyComponentSetLoadFailed Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_componentSet_
    The component set which failed.

Glossary Item Box

Called when a component set's root compoent could not be loaded. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyComponentSetLoadFailed( _
       ByVal _componentSet_ As [ProjectComponentSet](topic4106.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim componentSet As [ProjectComponentSet](topic4106.md)
     
    instance.NotifyComponentSetLoadFailed(componentSet)  
  
C#|   
---|---  
      
    
    void NotifyComponentSetLoadFailed( 
       [ProjectComponentSet](topic4106.md) _componentSet_
    )  
  
#### Parameters

 _componentSet_
    The component set which failed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


