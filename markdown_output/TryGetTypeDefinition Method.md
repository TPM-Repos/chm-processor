TryGetTypeDefinition Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectItemListDef Class](topic4511.md) : TryGetTypeDefinition Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_dialogName_
    

_typeDef_
    

Glossary Item Box

Gets the type definition for a specific dialog. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetTypeDefinition( _
       ByVal _dialogName_ As String, _
       ByRef _typeDef_ As [ProjectItemListTypeDef](topic4533.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectItemListDef](topic4511.md)
    Dim dialogName As String
    Dim typeDef As [ProjectItemListTypeDef](topic4533.md)
    Dim value As Boolean
     
    value = instance.TryGetTypeDefinition(dialogName, typeDef)  
  
C#|   
---|---  
      
    
    public bool TryGetTypeDefinition( 
       string _dialogName_ ,
       ref [ProjectItemListTypeDef](topic4533.md) _typeDef_
    )  
  
#### Parameters

 _dialogName_
    
_typeDef_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectItemListDef Class](topic4511.md)   
[ProjectItemListDef Members](topic4512.md)


