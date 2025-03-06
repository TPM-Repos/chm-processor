       

_TStep_
    

   
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetStep<TStep>(String,TStep) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Navigation Namespace](topic10114.md) > [ProjectNavigation Class](topic10222.md) > [TryGetStep Method](topic10243.md) : TryGetStep<TStep>(String,TStep) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the step to retrieve.

_navigationStep_
    A reference to a variable which will received the retrieved navigation step.

Glossary Item Box

Gets the named navigation step. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetStep(Of TStep As [NavigationStep](topic10175.md))( _
       ByVal _name_ As String, _
       ByRef _navigationStep_ As TStep _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectNavigation](topic10222.md)
    Dim name As String
    Dim navigationStep As TStep
    Dim value As Boolean
     
    value = instance.TryGetStep(Of TStep)(name, navigationStep)  
  
C#|   
---|---  
      
    
    public bool TryGetStep<TStep>( 
       string _name_ ,
       ref TStep _navigationStep_
    )
    where TStep: [NavigationStep](topic10175.md)  
  
#### Parameters

 _name_
    The name of the step to retrieve.
_navigationStep_
    A reference to a variable which will received the retrieved navigation step.

#### Type Parameters

_TStep_
    

#### Return Value

True if the item was successfully retrieved, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectNavigation Class](topic10222.md)   
[ProjectNavigation Members](topic10223.md)   
[Overload List](topic10243.md)


