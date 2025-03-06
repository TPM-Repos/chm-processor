![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ComponentTaskParameterMetaData Constructor(PropertyBehavior,Type,Object)   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskParameterMetaData Class](topic6619.md) > [ComponentTaskParameterMetaData Constructor](topic6625.md) : ComponentTaskParameterMetaData Constructor(PropertyBehavior,Type,Object)  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_behaviour_
    The behavior of the property.

_valueType_
    The CLR type of the property when it is static (if supported).

_defaultValue_
    The default value of the property when it has just been created.

Glossary Item Box

Creates a new instance of the [ComponentTaskParameterMetaData](topic6619.md) class. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function New( _
       ByVal _behaviour_ As [PropertyBehavior](topic9383.md), _
       ByVal _valueType_ As Type, _
       ByVal _defaultValue_ As Object _
    )  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim behaviour As [PropertyBehavior](topic9383.md)
    Dim valueType As Type
    Dim defaultValue As Object
     
    Dim instance As New [ComponentTaskParameterMetaData](topic6619.md)(behaviour, valueType, defaultValue)  
  
C#|   
---|---  
      
    
    public ComponentTaskParameterMetaData( 
       [PropertyBehavior](topic9383.md) _behaviour_ ,
       Type _valueType_ ,
       object _defaultValue_
    )  
  
#### Parameters

 _behaviour_
    The behavior of the property.
_valueType_
    The CLR type of the property when it is static (if supported).
_defaultValue_
    The default value of the property when it has just been created.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskParameterMetaData Class](topic6619.md)   
[ComponentTaskParameterMetaData Members](topic6620.md)   
[Overload List](topic6625.md)


