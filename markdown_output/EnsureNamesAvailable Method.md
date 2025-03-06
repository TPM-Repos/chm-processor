![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
EnsureNamesAvailable Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlCollection Class](topic7766.md) : EnsureNamesAvailable Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_deserialized_
    The deserialized control information, retrieved by using the [DriveWorks.Forms.DataModel.Serialization.ControlDeserializer](topic9604.md) class.

_renameDuplicates_
    True if duplicate controls should be renamed, false if an exception should be thrown instead.

Glossary Item Box

Ensures that the names of the given controls are not taken. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function EnsureNamesAvailable( _
       ByVal _deserialized_() As [ControlData](topic9593.md), _
       ByVal _renameDuplicates_ As Boolean _
    ) As [ControlData()](topic9593.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ControlCollection](topic7766.md)
    Dim deserialized() As [ControlData](topic9593.md)
    Dim renameDuplicates As Boolean
    Dim value() As [ControlData](topic9593.md)
     
    value = instance.EnsureNamesAvailable(deserialized, renameDuplicates)  
  
C#|   
---|---  
      
    
    public [ControlData[]](topic9593.md) EnsureNamesAvailable( 
       [ControlData](topic9593.md)[] _deserialized_ ,
       bool _renameDuplicates_
    )  
  
#### Parameters

 _deserialized_
    The deserialized control information, retrieved by using the [DriveWorks.Forms.DataModel.Serialization.ControlDeserializer](topic9604.md) class.
_renameDuplicates_
    True if duplicate controls should be renamed, false if an exception should be thrown instead.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ControlCollection Class](topic7766.md)   
[ControlCollection Members](topic7767.md)


