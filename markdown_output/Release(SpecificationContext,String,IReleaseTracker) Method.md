       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Release(SpecificationContext,String,IReleaseTracker) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentHelper Class](topic6275.md) > [Release Method](topic6281.md) : Release(SpecificationContext,String,IReleaseTracker) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The specification context for which to release components.

_components_
    The names of the components to release separated by commas, or a "*" to release all components.

_tracker_
    An implementation of the [IReleaseTracker](topic6119.md) interface, or a null reference.

Glossary Item Box

Releases the components specified by the given string and returns the results. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Release( _
       ByVal _context_ As [SpecificationContext](topic11149.md), _
       ByVal _components_ As String, _
       ByVal _tracker_ As [IReleaseTracker](topic6119.md) _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim context As [SpecificationContext](topic11149.md)
    Dim components As String
    Dim tracker As [IReleaseTracker](topic6119.md)
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = [ReleaseComponentHelper](topic6275.md).Release(context, components, tracker)  
  
C#|   
---|---  
      
    
    public static [ReleaseComponentsResults](topic6300.md) Release( 
       [SpecificationContext](topic11149.md) _context_ ,
       string _components_ ,
       [IReleaseTracker](topic6119.md) _tracker_
    )  
  
#### Parameters

 _context_
    The specification context for which to release components.
_components_
    The names of the components to release separated by commas, or a "*" to release all components.
_tracker_
    An implementation of the [IReleaseTracker](topic6119.md) interface, or a null reference.

#### Return Value

The release results.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentHelper Class](topic6275.md)   
[ReleaseComponentHelper Members](topic6276.md)   
[Overload List](topic6281.md)


