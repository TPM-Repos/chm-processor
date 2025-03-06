       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Start(IErrorHandler,IErrorHandler) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [RemoteGroupServer Class](topic5192.md) > [Start Method](topic5203.md) : Start(IErrorHandler,IErrorHandler) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_adminErrorHandler_
    

_connectionErrorHandler_
    

Glossary Item Box

Starts the underlying Remote Admin and Group Connection services. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Start( _
       ByVal _adminErrorHandler_ As IErrorHandler, _
       ByVal _connectionErrorHandler_ As IErrorHandler _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [RemoteGroupServer](topic5192.md)
    Dim adminErrorHandler As IErrorHandler
    Dim connectionErrorHandler As IErrorHandler
     
    instance.Start(adminErrorHandler, connectionErrorHandler)  
  
C#|   
---|---  
      
    
    public void Start( 
       IErrorHandler _adminErrorHandler_ ,
       IErrorHandler _connectionErrorHandler_
    )  
  
#### Parameters

 _adminErrorHandler_
    
_connectionErrorHandler_
    

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[RemoteGroupServer Class](topic5192.md)   
[RemoteGroupServer Members](topic5193.md)   
[Overload List](topic5203.md)


