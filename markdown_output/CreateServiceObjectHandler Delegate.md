Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateServiceObjectHandler Delegate   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : CreateServiceObjectHandler Delegate  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the service to create.

Glossary Item Box

Provides support for lazy creation of services. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Delegate Function CreateServiceObjectHandler( _
       ByVal _type_ As Type _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As New [CreateServiceObjectHandler](topic1268.md)(AddressOf HandlerMethod)  
  
C#|   
---|---  
      
    
    public delegate object CreateServiceObjectHandler( 
       Type _type_
    )  
  
#### Parameters

 _type_
    The type of the service to create.

#### Return Value

An instance of an object implementing the specified service, or a null reference (Nothing in Visual Basic) if the specified type is not supported.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CreateServiceObjectHandler Members](topic1268.md)   
[DriveWorks.Applications Namespace](topic16.md)


