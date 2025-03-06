![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertDistanceUnits Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [MeasurementHelper Class](topic3685.md) : ConvertDistanceUnits Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_sourceValue_
    The source value expressed in sourceUnits.

_sourceUnits_
    The units in which the source value is expressed.

_targetUnits_
    The units in to which to convert.

Glossary Item Box

Converts the given measurement of distance into an alternative representation. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function ConvertDistanceUnits( _
       ByVal _sourceValue_ As Double, _
       ByVal _sourceUnits_ As [DistanceMeasurementUnitOptions](topic2352.md), _
       ByVal _targetUnits_ As [DistanceMeasurementUnitOptions](topic2352.md) _
    ) As Double  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim sourceValue As Double
    Dim sourceUnits As [DistanceMeasurementUnitOptions](topic2352.md)
    Dim targetUnits As [DistanceMeasurementUnitOptions](topic2352.md)
    Dim value As Double
     
    value = [MeasurementHelper](topic3685.md).ConvertDistanceUnits(sourceValue, sourceUnits, targetUnits)  
  
C#|   
---|---  
      
    
    public static double ConvertDistanceUnits( 
       double _sourceValue_ ,
       [DistanceMeasurementUnitOptions](topic2352.md) _sourceUnits_ ,
       [DistanceMeasurementUnitOptions](topic2352.md) _targetUnits_
    )  
  
#### Parameters

 _sourceValue_
    The source value expressed in sourceUnits.
_sourceUnits_
    The units in which the source value is expressed.
_targetUnits_
    The units in to which to convert.

#### Return Value

The converted distance.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[MeasurementHelper Class](topic3685.md)   
[MeasurementHelper Members](topic3686.md)


