![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxRecreateFormControl(Form,ContainerControlBase,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13119.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) > [CreateTxRecreateFormControl Method](topic13118.md) : CreateTxRecreateFormControl(Form,ContainerControlBase,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_form_
    The form to create the controls on.

_parent_
    The parent control to create the controls in.

_controlSerializationData_
    The pasted serialized text for the controls.

Glossary Item Box

Creates a transaction Create new controls from the given serialized text. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateTxRecreateFormControl( _
       ByVal _form_ As [Form](topic8086.md), _
       ByVal _parent_ As [ContainerControlBase](topic7684.md), _
       ByVal _controlSerializationData_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim form As [Form](topic8086.md)
    Dim parent As [ContainerControlBase](topic7684.md)
    Dim controlSerializationData As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxRecreateFormControl(form, parent, controlSerializationData)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxRecreateFormControl( 
       [Form](topic8086.md) _form_ ,
       [ContainerControlBase](topic7684.md) _parent_ ,
       string _controlSerializationData_
    )  
  
#### Parameters

 _form_
    The form to create the controls on.
_parent_
    The parent control to create the controls in.
_controlSerializationData_
    The pasted serialized text for the controls.

#### Return Value

A transaction

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)   
[Overload List](topic13118.md)

©2024 DriveWorks Ltd. All Rights Reserved.
