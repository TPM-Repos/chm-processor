Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
PreProcessReleaseData Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedSolidWorksComponent Class](topic15029.md) : PreProcessReleaseData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_controller_
    

_data_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub PreProcessReleaseData( _
       ByVal _controller_ As [ReleaseComponentController](topic6252.md), _
       ByVal _data_ As ReleasedComponentData _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedSolidWorksComponent](topic15029.md)
    Dim controller As [ReleaseComponentController](topic6252.md)
    Dim data As ReleasedComponentData
     
    instance.PreProcessReleaseData(controller, data)  
  
C#|   
---|---  
      
    
    protected override void PreProcessReleaseData( 
       [ReleaseComponentController](topic6252.md) _controller_ ,
       ReleasedComponentData _data_
    )  
  
#### Parameters

 _controller_
    
_data_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedSolidWorksComponent Class](topic15029.md)   
[ReleasedSolidWorksComponent Members](topic15030.md)


