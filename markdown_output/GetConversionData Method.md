Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetConversionData Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ICanConvert Interface](topic7268.md) : GetConversionData Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_newType_
    The type of control to convert this control to.

Glossary Item Box

Returns a [DriveWorks.Forms.DataModel.Serialization.ControlData](topic9593.md) that when added to a [ContainerControlBase](topic7684.md) will create a new control of the given type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function GetConversionData( _
       ByVal _newType_ As Type _
    ) As [ControlData](topic9593.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICanConvert](topic7268.md)
    Dim newType As Type
    Dim value As [ControlData](topic9593.md)
     
    value = instance.GetConversionData(newType)  
  
C#|   
---|---  
      
    
    [ControlData](topic9593.md) GetConversionData( 
       Type _newType_
    )  
  
#### Parameters

 _newType_
    The type of control to convert this control to.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICanConvert Interface](topic7268.md)   
[ICanConvert Members](topic7269.md)


