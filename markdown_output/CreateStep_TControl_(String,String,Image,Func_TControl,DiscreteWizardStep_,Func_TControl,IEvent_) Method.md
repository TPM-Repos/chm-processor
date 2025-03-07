_TControl_
    

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateStep<TControl>(String,String,Image,Func<TControl,DiscreteWizardStep>,Func<TControl,IEvent>) Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [DiscreteWizardBase Class](topic737.md) > [CreateStep Method](topic744.md) : CreateStep<TControl>(String,String,Image,Func<TControl,DiscreteWizardStep>,Func<TControl,IEvent>) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the step.

_description_
    The description of the step.

_image_
    The step's image.

_getNextStepMethod_
    A method which will get the next step.

_getNextStepChangedEventProxyMethod_
    A method which will get an event which can be used to determine when the next step has changed.

Glossary Item Box

Creates a new instance of the **DiscreteWizardStep`2** class. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overloads Function CreateStep(Of TControl As Control)( _
       ByVal _title_ As String, _
       ByVal _description_ As String, _
       ByVal _image_ As Image, _
       ByVal _getNextStepMethod_ As Func(Of TControl,DiscreteWizardStep), _
       ByVal _getNextStepChangedEventProxyMethod_ As Func(Of TControl,IEvent) _
    ) As [DiscreteWizardStep(Of TControl)](topic770.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [DiscreteWizardBase](topic737.md)
    Dim title As String
    Dim description As String
    Dim image As Image
    Dim getNextStepMethod As Func(Of TControl,DiscreteWizardStep)
    Dim getNextStepChangedEventProxyMethod As Func(Of TControl,IEvent)
    Dim value As [DiscreteWizardStep(Of TControl)](topic770.md)
     
    value = instance.CreateStep(Of TControl)(title, description, image, getNextStepMethod, getNextStepChangedEventProxyMethod)  
  
C#|   
---|---  
      
    
    protected [DiscreteWizardStep<TControl>](topic770.md) CreateStep<TControl>( 
       string _title_ ,
       string _description_ ,
       Image _image_ ,
       Func<TControl,DiscreteWizardStep> _getNextStepMethod_ ,
       Func<TControl,IEvent> _getNextStepChangedEventProxyMethod_
    )
    where TControl: Control  
  
#### Parameters

 _title_
    The title of the step.
_description_
    The description of the step.
_image_
    The step's image.
_getNextStepMethod_
    A method which will get the next step.
_getNextStepChangedEventProxyMethod_
    A method which will get an event which can be used to determine when the next step has changed.

#### Type Parameters

_TControl_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[DiscreteWizardBase Class](topic737.md)   
[DiscreteWizardBase Members](topic738.md)   
[Overload List](topic744.md)


