![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
ConvertStringToDateTime(Object,CultureInfo) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms.DataModel Namespace](topic9371.md) > [StoreConverter Class](topic9528.md) > [ConvertStringToDateTime Method](topic9553.md) : ConvertStringToDateTime(Object,CultureInfo) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_value_
    The source value.

_culture_
    

Glossary Item Box

Converts the specified string to a date-time. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function ConvertStringToDateTime( _
       ByVal _value_ As Object, _
       ByVal _culture_ As CultureInfo _
    ) As Object  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim value As Object
    Dim culture As CultureInfo
    Dim value As Object
     
    value = [StoreConverter](topic9528.md).ConvertStringToDateTime(value, culture)  
  
C#|   
---|---  
      
    
    public static object ConvertStringToDateTime( 
       object _value_ ,
       CultureInfo _culture_
    )  
  
#### Parameters

 _value_
    The source value.
_culture_
    

#### Return Value

A date/time.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[StoreConverter Class](topic9528.md)   
[StoreConverter Members](topic9529.md)   
[Overload List](topic9553.md)


