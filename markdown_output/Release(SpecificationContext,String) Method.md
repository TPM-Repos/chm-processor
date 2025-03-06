Release(SpecificationContext,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentHelper Class](topic6275.md) > [Release Method](topic6281.md) : Release(SpecificationContext,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The specification context for which to release components.

_components_
    The names of the components to release separated by commas, or a "*" to release all components.

Glossary Item Box

Releases the components specified by the given string and returns the results. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Release( _
       ByVal _context_ As [SpecificationContext](topic11149.md), _
       ByVal _components_ As String _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim context As [SpecificationContext](topic11149.md)
    Dim components As String
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = [ReleaseComponentHelper](topic6275.md).Release(context, components)  
  
C#|   
---|---  
      
    
    public static [ReleaseComponentsResults](topic6300.md) Release( 
       [SpecificationContext](topic11149.md) _context_ ,
       string _components_
    )  
  
#### Parameters

 _context_
    The specification context for which to release components.
_components_
    The names of the components to release separated by commas, or a "*" to release all components.

#### Return Value

The release results.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleaseComponentHelper Class](topic6275.md)   
[ReleaseComponentHelper Members](topic6276.md)   
[Overload List](topic6281.md)


