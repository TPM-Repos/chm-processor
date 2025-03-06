       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TrackParameterRelease Method   
  
[DriveWorks.SolidWorks Assembly](topic13342.md) > [DriveWorks.SolidWorks.Components Namespace](topic13925.md) > [ReleasedDrawing Class](topic14859.md) : TrackParameterRelease Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_tracker_
    

_parameter_
    

_value_
    

Glossary Item Box

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overrides Sub TrackParameterRelease( _
       ByVal _tracker_ As [IReleaseParameterTracker](topic6113.md), _
       ByVal _parameter_ As ProjectParameterData, _
       ByVal _value_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ReleasedDrawing](topic14859.md)
    Dim tracker As [IReleaseParameterTracker](topic6113.md)
    Dim parameter As ProjectParameterData
    Dim value As String
     
    instance.TrackParameterRelease(tracker, parameter, value)  
  
C#|   
---|---  
      
    
    protected override void TrackParameterRelease( 
       [IReleaseParameterTracker](topic6113.md) _tracker_ ,
       ProjectParameterData _parameter_ ,
       string _value_
    )  
  
#### Parameters

 _tracker_
    
_parameter_
    
_value_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ReleasedDrawing Class](topic14859.md)   
[ReleasedDrawing Members](topic14860.md)


