ReleaseFeature Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSolidWorksComponent Class](topic15029.md) : ReleaseFeature Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controller_
    

_data_
    

_elem_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Shared Sub ReleaseFeature( _
       ByVal _controller_ As [ReleaseComponentController](topic6252.md), _
       ByVal _data_ As ReleasedComponentData, _
       ByVal _elem_ As ReleasedElementData _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim controller As [ReleaseComponentController](topic6252.md)
    Dim data As ReleasedComponentData
    Dim elem As ReleasedElementData
     
    [ReleasedSolidWorksComponent](topic15029.md).ReleaseFeature(controller, data, elem)  
  
C#|   
---|---  
      
    
    protected static void ReleaseFeature( 
       [ReleaseComponentController](topic6252.md) _controller_ ,
       ReleasedComponentData _data_ ,
       ReleasedElementData _elem_
    )  
  
#### Parameters

 _controller_
    
_data_
    
_elem_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedSolidWorksComponent Class](topic15029.md)   
[ReleasedSolidWorksComponent Members](topic15030.md)


