       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ReleaseDimension Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSolidWorksComponent Class](topic15029.md) : ReleaseDimension Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controller_
    

_data_
    

_param_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Shared Sub ReleaseDimension( _
       ByVal _controller_ As [ReleaseComponentController](topic6252.md), _
       ByVal _data_ As ReleasedComponentData, _
       ByVal _param_ As ReleasedParameterData _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim controller As [ReleaseComponentController](topic6252.md)
    Dim data As ReleasedComponentData
    Dim param As ReleasedParameterData
     
    [ReleasedSolidWorksComponent](topic15029.md).ReleaseDimension(controller, data, param)  
  
C#|   
---|---  
      
    
    protected static void ReleaseDimension( 
       [ReleaseComponentController](topic6252.md) _controller_ ,
       ReleasedComponentData _data_ ,
       ReleasedParameterData _param_
    )  
  
#### Parameters

 _controller_
    
_data_
    
_param_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedSolidWorksComponent Class](topic15029.md)   
[ReleasedSolidWorksComponent Members](topic15030.md)


