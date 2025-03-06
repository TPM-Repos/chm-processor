![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanConvertTo(ITypeDescriptorContext,Type) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3478.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [IArrayValueConverter Class](topic3468.md) > [CanConvertTo Method](topic3477.md) : CanConvertTo(ITypeDescriptorContext,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    

_destinationType_
    

Glossary Item Box

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Overrides Function CanConvertTo( _
       ByVal _context_ As ITypeDescriptorContext, _
       ByVal _destinationType_ As Type _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IArrayValueConverter](topic3468.md)
    Dim context As ITypeDescriptorContext
    Dim destinationType As Type
    Dim value As Boolean
     
    value = instance.CanConvertTo(context, destinationType)  
  
C#|   
---|---  
      
    
    public override bool CanConvertTo( 
       ITypeDescriptorContext _context_ ,
       Type _destinationType_
    )  
  
#### Parameters

 _context_
    
_destinationType_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IArrayValueConverter Class](topic3468.md)   
[IArrayValueConverter Members](topic3469.md)   
[Overload List](topic3477.md)

©2024 DriveWorks Ltd. All Rights Reserved.
