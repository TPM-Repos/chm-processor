Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RaisePropertyChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [ProcessActionBase Class](topic9935.md) : RaisePropertyChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_propertyName_
    The name of the property that has changed.

Glossary Item Box

Raises the [PropertyChanged](topic9948.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Sub RaisePropertyChanged( _
       ByVal _propertyName_ As String _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProcessActionBase](topic9935.md)
    Dim propertyName As String
     
    instance.RaisePropertyChanged(propertyName)  
  
C#|   
---|---  
      
    
    protected void RaisePropertyChanged( 
       string _propertyName_
    )  
  
#### Parameters

 _propertyName_
    The name of the property that has changed.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProcessActionBase Class](topic9935.md)   
[ProcessActionBase Members](topic9936.md)


