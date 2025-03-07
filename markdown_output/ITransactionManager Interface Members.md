Collapse All Expand All Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
ITransactionManager Interface Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic502.md)  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) : ITransactionManager Interface  
---  
  
Include Inherited Members    


Glossary Item Box

The following tables list the members exposed by [ITransactionManager](topic502.md).

# Public Properties

| Name| Description  
---|---|---  
![ Property](dotnetimages/Property.gif)| [CanRedo](topic512.md)| Gets a value indicating whether there are any transactions in the redo chain.   
![ Property](dotnetimages/Property.gif)| [CanUndo](topic513.md)| Gets a value indicating whether there are any transactions in the undo chain.   
![ Property](dotnetimages/Property.gif)| [UndoRedoEnabled](topic514.md)| Gets or sets whether or not the user can use the undo and redo buttons.   
Top

# Public Methods

| Name| Description  
---|---|---  
![ Method](dotnetimages/Method.gif)| [ClearAllHistory](topic507.md)| Clears the transaction history of all views.   
![ Method](dotnetimages/Method.gif)| [ClearHistory](topic508.md)| Clears the transaction history.   
![ Method](dotnetimages/Method.gif)| [Redo](topic509.md)| Redoes the last transaction in the redo chain.   
![ Method](dotnetimages/Method.gif)| [RegisterTransaction](topic510.md)| Register's a transaction with the transaction manager's undo chain.   
![ Method](dotnetimages/Method.gif)| [Undo](topic511.md)| Undoes the last transaction in the undo chain.   
Top

# Public Events

| Name| Description  
---|---|---  
![ Event](dotnetimages/Event.gif)| [TransactionCommitted](topic515.md)| Raised when a transaction is committed.   
![ Event](dotnetimages/Event.gif)| [TransactionExecuting](topic516.md)| Raised before an historical transaction is executed.   
![ Event](dotnetimages/Event.gif)| [TransactionHistoryCleared](topic517.md)| Raised after the transaction history has been cleared.   
![ Event](dotnetimages/Event.gif)| [TransactionRolledBack](topic518.md)| Raised when a transaction is rolled back.   
Top

# See Also

#### Reference

[ITransactionManager Interface](topic502.md)   
[DriveWorks.Applications Namespace](topic16.md)


