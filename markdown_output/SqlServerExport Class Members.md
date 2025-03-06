       

 Collapse All Expand All  Members Options: Show All  Members Options: Filtered   
---  
DriveWorks SDK Documentation  |   
---|---  
SqlServerExport Class Members   
See Also Properties Methods Events [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic5417.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) : SqlServerExport Class  
---  
  
Include Inherited Members    
Include Protected Members  


Glossary Item Box

The following tables list the members exposed by [SqlServerExport](topic5417.md).

# Public Properties

| Name| Description  
---|---|---  
![Public Property](dotnetimages/publicProperty.gif)| [Columns](topic5435.md)| Gets an array of all the columns that are used in the table.   
![Public Property](dotnetimages/publicProperty.gif)| [CommonColumns](topic5436.md)| Gets A collection of common columns. Common columns are always the same for each row. Used to save calculation time.   
![Public Property](dotnetimages/publicProperty.gif)| [ControlColumns](topic5437.md)| Gets a collection of control columns. Control columns depict where export row data is to match the existing data for updating/appending rows.   
![Public Property](dotnetimages/publicProperty.gif)| [DatabaseName](topic5438.md)| Gets/Sets the name of the SQL server database to connect to.   
![Public Property](dotnetimages/publicProperty.gif)| [DatabaseNameRule](topic5439.md)| Gets the [ProjectDocumentRule](topic4399.md) for the database segment of the document export.   
![Public Property](dotnetimages/publicProperty.gif)| [ExportWhen](topic5440.md)| Gets/Sets when the data will be exported during the specification.   
![Public Property](dotnetimages/publicProperty.gif)| [HasDisplayFileRule](topic4391.md)| Gets whether the document has a display file rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsDeleted](topic4392.md)| Gets whether the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [IsInitialized](topic4393.md)| Gets whether the document has been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Name](topic4394.md)| Gets/sets the name of the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Password](topic5441.md)| Gets/Sets the Password that is used to connect to the SQL Server.   
![Public Property](dotnetimages/publicProperty.gif)| [PasswordRule](topic5442.md)| Gets the [ProjectDocumentRule](topic4399.md) for the password segment of the document export.   
![Public Property](dotnetimages/publicProperty.gif)| [Project](topic4395.md)| Gets the project to which the document belongs. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [Rows](topic5443.md)| Gets all of the new rows that will be updated or append the table.   
![Public Property](dotnetimages/publicProperty.gif)| [ServerName](topic5444.md)| Gets/Sets the name of the SQL server to connect to.   
![Public Property](dotnetimages/publicProperty.gif)| [ServerPathRule](topic5445.md)| Gets the [ProjectDocumentRule](topic4399.md) for the server path segment of the document export.   
![Public Property](dotnetimages/publicProperty.gif)| [SupportsPreview](topic4396.md)| Gets whether the document supports generating a preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Property](dotnetimages/publicProperty.gif)| [TableName](topic5446.md)| Gets/Sets the name of the table to connect to.   
![Public Property](dotnetimages/publicProperty.gif)| [UserName](topic5447.md)| Gets/Sets the Username that is used to connect to the SQL Server.   
![Public Property](dotnetimages/publicProperty.gif)| [UserNameRule](topic5448.md)| Gets the [ProjectDocumentRule](topic4399.md) for the username segment of the document export.   
![Public Property](dotnetimages/publicProperty.gif)| [WindowsAuthentication](topic5449.md)| Determines whether to use Windows Authentication to connect to the SQL Server.   
Top

# Protected Properties

| Name| Description  
---|---|---  
![Protected Property](dotnetimages/protectedProperty.gif)| [Data](topic4390.md)| Gets/sets the custom data for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# Public Methods

| Name| Description  
---|---|---  
![Public Method](dotnetimages/publicMethod.gif)| [AddColumn](topic5423.md)| Adds a column that is present in the target table.   
![Public Method](dotnetimages/publicMethod.gif)| [AddCommonColumn](topic5424.md)| Adds a common column to the table.   
![Public Method](dotnetimages/publicMethod.gif)| [AddRow](topic5425.md)| Adds a row to the list of export rows.   
![Public Method](dotnetimages/publicMethod.gif)| [ClearColumns](topic5426.md)| Removes all column specifications.   
![Public Method](dotnetimages/publicMethod.gif)| [ClearRows](topic5427.md)| Removes all rows from the list of export rows.   
![Public Method](dotnetimages/publicMethod.gif)| CreateObjRef|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [Delete](topic4368.md)| Deletes the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [Generate](topic4372.md)| Generates the document within the context of the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GeneratePreview](topic4374.md)| Overloaded. Creates a preview of the document in the specified directory. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Method](dotnetimages/publicMethod.gif)| [GetExportSummary](topic5429.md)| Retrieve the generation summary for the document in a specifications test mode.   
![Public Method](dotnetimages/publicMethod.gif)| GetLifetimeService|  (Inherited from System.MarshalByRefObject)  
![Public Method](dotnetimages/publicMethod.gif)| [RemoveRow](topic5432.md)| Removes a row from the list of rows to be exported.   
![Public Method](dotnetimages/publicMethod.gif)| [ShouldGenerate](topic5433.md)| Overloaded. Overridden. Determines whether the document should be generated.   
![Public Method](dotnetimages/publicMethod.gif)| [ShouldGeneratePreview](topic4386.md)| Overloaded. Determines whether the document should be generated during preview. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# Protected Methods

| Name| Description  
---|---|---  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertInitialized](topic4362.md)| Throws an exception if the document hasn't been initialized. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [AssertNotDeleted](topic4363.md)| Throws an exception if the document has been deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [CalculateRules](topic4364.md)| Overloaded. Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [CalculateRulesCore](topic4367.md)| Calculates the results of the rules that have been defined for the document. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [DeleteCore](topic4369.md)| When overridden in a derived class, performs any clean-up necessary to delete the document from the project. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [EvaluateRule](topic4371.md)| Evaluates the specified rule formula into a displayable string. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GenerateCore](topic5428.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [GeneratePreviewCore](topic4377.md)| When overridden in a derived class, generates a preview of the document in the specified directory using the given calculated rule results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [GetResultForRuleAsDisplayString](topic4378.md)| Gets the specified rule as a string from the calculated results. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeExistingCore](topic5430.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| [InitializeNewCore](topic5431.md)| Overridden.   
![Protected Method](dotnetimages/protectedMethod.gif)| MemberwiseClone| Overloaded. (Inherited from System.MarshalByRefObject)  
![Protected Method](dotnetimages/protectedMethod.gif)| [RegisterSpecificationDocument](topic4381.md)| Registers a new specification document with the active specification. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [SetRuleContext](topic4382.md)| Sets a rule context that will be use by the Titan rule engine when evaluating the rule. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Protected Method](dotnetimages/protectedMethod.gif)| [ThrowCorruptDocumentDataException](topic4389.md)| Throws the [CorruptDocumentDataException](topic2624.md) exception. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# Public Events

| Name| Description  
---|---|---  
![Public Event](dotnetimages/publicEvent.gif)| [Deleted](topic4397.md)| Raised when the document is deleted. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
![Public Event](dotnetimages/publicEvent.gif)| [NameChanged](topic4398.md)| Raised when the document's name changes. (Inherited from [DriveWorks.ProjectDocument](topic4356.md))  
Top

# See Also

#### Reference

[SqlServerExport Class](topic5417.md)   
[DriveWorks Namespace](topic2159.md)

©2024 DriveWorks Ltd. All Rights Reserved.
