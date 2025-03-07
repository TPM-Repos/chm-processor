Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EvaluateDistanceMeasurement Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectUtility Class](topic4899.md) : EvaluateDistanceMeasurement Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_measurement_
    A measurement string, for example "(4 + 5)ft 3' 7mm"

_desiredUnits_
    The units to convert the result into.

Glossary Item Box

Evaluates the given measurement string and returns the result in the specified units. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EvaluateDistanceMeasurement( _
       ByVal _measurement_ As String, _
       ByVal _desiredUnits_ As [DistanceMeasurementUnitOptions](topic2352.md) _
    ) As Double  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectUtility](topic4899.md)
    Dim measurement As String
    Dim desiredUnits As [DistanceMeasurementUnitOptions](topic2352.md)
    Dim value As Double
     
    value = instance.EvaluateDistanceMeasurement(measurement, desiredUnits)  
  
C#|   
---|---  
      
    
    public double EvaluateDistanceMeasurement( 
       string _measurement_ ,
       [DistanceMeasurementUnitOptions](topic2352.md) _desiredUnits_
    )  
  
#### Parameters

 _measurement_
    A measurement string, for example "(4 + 5)ft 3' 7mm"
_desiredUnits_
    The units to convert the result into.

#### Return Value

The value of the measurement in the specified units.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectUtility Class](topic4899.md)   
[ProjectUtility Members](topic4900.md)


