![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Deserialize Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9610.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel.Serialization Namespace](topic9591.md) > [ControlDeserializer Class](topic9604.md) : Deserialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_reader_
    The XML reader which is positioned before the start of the control element.

_typeResolver_
    The type resolver used to retrieve CLR types for controls.

_deserializeInvariant_
    True to deserialize the control property values invariantly, otherwise False to deserialize them using the current culture.

Glossary Item Box

Deserializes the control in the specified XML reader. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Shared Function Deserialize( _
       ByVal _reader_ As XmlReader, _
       ByVal _typeResolver_ As [ControlTypeResolverDelegate](topic9625.md), _
       ByVal _deserializeInvariant_ As Boolean _
    ) As [ControlData()](topic9593.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim reader As XmlReader
    Dim typeResolver As [ControlTypeResolverDelegate](topic9625.md)
    Dim deserializeInvariant As Boolean
    Dim value() As [ControlData](topic9593.md)
     
    value = [ControlDeserializer](topic9604.md).Deserialize(reader, typeResolver, deserializeInvariant)  
  
C#|   
---|---  
      
    
    public static [ControlData[]](topic9593.md) Deserialize( 
       XmlReader _reader_ ,
       [ControlTypeResolverDelegate](topic9625.md) _typeResolver_ ,
       bool _deserializeInvariant_
    )  
  
#### Parameters

 _reader_
    The XML reader which is positioned before the start of the control element.
_typeResolver_
    The type resolver used to retrieve CLR types for controls.
_deserializeInvariant_
    True to deserialize the control property values invariantly, otherwise False to deserialize them using the current culture.

#### Return Value

The deserialized control data.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlDeserializer Class](topic9604.md)   
[ControlDeserializer Members](topic9605.md)

©2024 DriveWorks Ltd. All Rights Reserved.
