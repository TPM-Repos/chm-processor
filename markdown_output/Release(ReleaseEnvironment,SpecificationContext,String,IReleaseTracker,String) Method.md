![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Release(ReleaseEnvironment,SpecificationContext,String,IReleaseTracker,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6288.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentHelper Class](topic6275.md) > [Release Method](topic6281.md) : Release(ReleaseEnvironment,SpecificationContext,String,IReleaseTracker,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_environment_
    The environment which controls the release process.

_context_
    The specification context for which to release components.

_components_
    The names of the components to release separated by a pipe-bar '|', or a "*" to release all components.

_tracker_
    An implementation of the [IReleaseTracker](topic6119.md) interface, or a null reference.

_derivedComponentsToDefer_
    The names of the derived components to put on hold, not to be generated at the same time as the associated models.

Glossary Item Box

Releases the components specified by the given string and returns the results. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Release( _
       ByVal _environment_ As [ReleaseEnvironment](topic6379.md), _
       ByVal _context_ As [SpecificationContext](topic11149.md), _
       ByVal _components_ As String, _
       ByVal _tracker_ As [IReleaseTracker](topic6119.md), _
       ByVal _derivedComponentsToDefer_ As String _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim environment As [ReleaseEnvironment](topic6379.md)
    Dim context As [SpecificationContext](topic11149.md)
    Dim components As String
    Dim tracker As [IReleaseTracker](topic6119.md)
    Dim derivedComponentsToDefer As String
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = [ReleaseComponentHelper](topic6275.md).Release(environment, context, components, tracker, derivedComponentsToDefer)  
  
C#|   
---|---  
      
    
    public static [ReleaseComponentsResults](topic6300.md) Release( 
       [ReleaseEnvironment](topic6379.md) _environment_ ,
       [SpecificationContext](topic11149.md) _context_ ,
       string _components_ ,
       [IReleaseTracker](topic6119.md) _tracker_ ,
       string _derivedComponentsToDefer_
    )  
  
#### Parameters

 _environment_
    The environment which controls the release process.
_context_
    The specification context for which to release components.
_components_
    The names of the components to release separated by a pipe-bar '|', or a "*" to release all components.
_tracker_
    An implementation of the [IReleaseTracker](topic6119.md) interface, or a null reference.
_derivedComponentsToDefer_
    The names of the derived components to put on hold, not to be generated at the same time as the associated models.

#### Return Value

The release results.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentHelper Class](topic6275.md)   
[ReleaseComponentHelper Members](topic6276.md)   
[Overload List](topic6281.md)

©2024 DriveWorks Ltd. All Rights Reserved.
